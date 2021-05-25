<template>
<div>
  <div v-if="this.editable">
    <input type="text" id="recherche" v-model="texteRecherche" @keyup="lancerRecherche"/>
    <div id="resutats-recherche">
    <p v-for="(item, index) in resultatsRecherche"
    @click="ajouterItem(resultatsRecherche[index].nom, resultatsRecherche[index].prix, resultatsRecherche[index].id)" :key="index">
    {{resultatsRecherche[index].nom}}</p>
    </div>
  </div>
    <div><ligne @maj="onMaj" v-for="(item, index) in items" :key="index" :id="item.id" :nom="item.nom" :prix="item.prix" :editable="editable"/></div>
{{total}}
<button v-if="this.editable" @click="sauvegarder">Sauvegarder</button>
</div>

</template>

<script>
import Ligne from '../components/Ligne.vue'

export default {
  name: 'liste',
  components: {
    Ligne
  },
  data: function () {
    let id = this.$route.query.id
    const listes = localStorage.getItem('listes')
    const donnees = JSON.parse(listes)
    id = parseInt(id)
    return {
      items: donnees[id].items,
      editable: donnees[id].editable,
      texteRecherche: '',
      resultatsRecherche: []
    }
  },
  computed: {
    total: function () {
      let total = 0
      this.items.forEach(function (item) { total += item.qte * item.prix })
      return total
    }
  },
  methods: {
    onMaj: function (id, valeur) {
      console.log(id + ' ' + valeur)
      const items = this.items
      console.log(items)
      for (let i = 0; i < items.length; i++) {
        if (items[i].id === id) {
          items[i].qte = valeur
        }
      }
    },
    ajouterItem: function (nom, prix, id) {
      this.items.push({ id, nom, prix, qte: 1 })
    },
    sauvegarder: function () {
      let listes = localStorage.getItem('listes')
      listes = JSON.parse(listes)
      const id = this.$route.query.id
      listes[id].items = this.items
      listes[id].editable = false
      localStorage.setItem('listes', JSON.stringify(listes))
      this.$router.push('/')
    },
    lancerRecherche: function () {
      if (this.texteRecherche !== '') {
        const self = this
        window.$.ajax({
          url: window.urlServiceWeb + 'items/' + self.texteRecherche,
          success: function (donnees) {
            self.resultatsRecherche = JSON.parse(donnees)
          }
        })
      } else {
        this.resultatsRecherche = []
      }
    }
  }
}
</script>

<style>

</style>

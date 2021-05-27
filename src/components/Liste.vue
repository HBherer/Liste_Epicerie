<template>
<div>
  <div class="displayFlexNoR">
    <div class="addItem">
      <h2 v-if="this.editable == false">Votre liste d'épicerie</h2>
      <div v-if="this.editable">
        <h2>Remplir votre liste</h2>
        <label class="h3" for="recherche">Entrez l'item recherché</label>
        <input type="text" class="inputRecherche" id="recherche" name="recherche" v-model="texteRecherche" @keyup="lancerRecherche"/>
        <div id="resutats-recherche">
          <h3>Article(s):</h3>
          <p class="resultItems" v-for="(item, index) in resultatsRecherche"
             @click="ajouterItem(resultatsRecherche[index].nom, resultatsRecherche[index].prix, resultatsRecherche[index].id)" :key="index">
            {{resultatsRecherche[index].nom}}</p>
        </div>
      </div>
    </div>
    <div class="validationList lightText">
      <div class="sec1">
        <h2 class="validationListTop">Sommaire</h2>
        <p class="h2">Coût total: {{total}} $</p>
        <button class="btnSecondary" v-if="this.editable" @click="sauvegarder">Sauvegarder</button>
      </div>
      <div class="imgAddItemList">
        <img src="/img/imgApp/facture.png">
      </div>
    </div>
    <div class="contentList">
      <h3>Vos item(s)</h3>
      <ligne @maj="onMaj" v-for="(item, index) in items" :key="index" :id="item.id" :nom="item.nom" :prix="item.prix" :editable="editable"/>
    </div>
  </div>
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
        this.resultatsRecherche = [
          { nom: 'Tomate', prix: '2', id: '1' },
          { nom: 'Poire', prix: '3', id: '2' },
          { nom: 'Orange', prix: '1', id: '3' },
          { nom: 'Pomme', prix: '2', id: '4' },
          { nom: 'Mangue', prix: '4', id: '5' },
          { nom: 'Raisin', prix: '1', id: '6' },
          { nom: 'Peche', prix: '2', id: '7' }
        ]
      }
    },
    showNav: function () {
      var nav = document.getElementById('showNavC')
      if (nav.classList.contains('displayBlock') === true) {
        nav.classList.remove('displayBlock')
        nav.classList.add('displayNone')
      } else {
        nav.classList.remove('displayNone')
        nav.classList.add('displayBlock')
      }
    }
  }
}
</script>

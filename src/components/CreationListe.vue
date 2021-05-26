<template>
<div>
  <div class="topNav">
    <div><router-link class="logo" to="/">ListeÉpicerie</router-link></div>
    <p><router-link class="btnPrimary seeListG" to="/voir-tous">Voir tous les produits</router-link></p>
    <img @click=showNav() class="seeHambergerNav" src="/img/imgApp/bergerNav.png">
    <span id="showNavC" class="contentNav displayNone">
      <p><router-link class="navLink lightText" to="/voir-tous">Voir tous les produits</router-link></p>
    </span>
  </div>
  <div class="creatList">
    <h2>Nouvelle liste d'épicerie</h2>
    <div>
      <input class="enterNameList" type="text" v-model="nom"/>
      <button type="submit" @click=creerListe>Créer</button>
    </div>
    <div class="imgCreatListe">
      <img class="" src="/img/imgApp/document.png">
    </div>
  </div>

</div>

</template>

<script>

export default {
  name: 'creerListe',
  data: function () {
    return { nom: '' }
  },
  methods: {
    creerListe: function () {
      // Faire vos validation javascript ici si vous ne prenez pas jQuery Validate
      let listes = localStorage.getItem('listes')
      let id
      if (listes === null) {
        listes = []
        id = 0
      } else {
        listes = JSON.parse(listes)
        id = listes.length
      }
      listes.push({ nom: this.nom, items: [], editable: true })
      localStorage.setItem('listes', JSON.stringify(listes))
      this.$router.push({ path: '/liste', query: { id: id } })
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

<style>

</style>

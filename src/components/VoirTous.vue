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
    <div>
      Nombre de produits : {{produits.length}}
      <div id="produits">
        <p v-for="(produits, index) in produits" :key="index">{{produits.nom}} - {{produits.prix}} $
        </p>
      </div>
    </div>

  </div>

</template>

<script>

export default {
  name: 'listeToutes',
  data: function () {
    return {
      produits: []
    }
  },
  mounted: function () {
    const self = this
    window.$.ajax({
      url: window.urlServiceWeb + 'items',
      success: function (donnees) {
        self.produits = JSON.parse(donnees)
      }
    })
  },
  methods: {
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

<template>
  <div id="app">
    <div class="topNav">
      <div class="logoPosition">
        <img class="imgLogo" src="img/icons/android-chrome-512x512.png">
        <p class="logo"><router-link class="router-link" to="/">ListeÉpicerie</router-link></p>
      </div>
      <p><router-link class="btnPrimary seeListG" to="/voir-tous">Voir tous les produits</router-link></p>
      <img @click=showNav() class="seeHambergerNav" src="/img/imgApp/bergerNav.png">
      <span id="showNavC" class="contentNav displayNone">
      <p><router-link class="navLink lightText" to="/voir-tous">Voir tous les produits</router-link></p>
    </span>
    </div>
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'App',
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  flex-wrap: wrap;
  color: #2c3e50;
  margin: 20px 60px;
}
</style>

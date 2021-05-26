<template>
<div>
  <div class="topNav">
    <div class="logo">ListeÉpicerie</div>
    <p><router-link class="btnPrimary seeListG" to="/voir-tous">Voir tous les produits</router-link></p>
    <img @click=showNav() class="seeHambergerNav" src="/img/imgApp/bergerNav.png">
    <span id="showNavC" class="contentNav displayNone">
      <p><router-link class="navLink lightText" to="/voir-tous">Voir tous les produits</router-link></p>
    </span>
  </div>
<div class="displayFlex">
  <div class="lists">
    <h2>Listes</h2>
    <div v-for="(liste, index) in this.donnees" :key="index" >
      <p>
        <router-link class="h3 titleSection" :to="{ path: 'liste', query: { id: index }}">
          {{liste.nom}}
        </router-link>
      </p>
      <div class="ligne"></div>
    </div>
  </div>
  <div class="addListe">
    <h2 class="lightText">Créer votre liste d'épicerie en ligne</h2>
    <div class="addListeSecG">
      <p class="texteAddList lightText">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
      </p>
      <p><router-link class="btnSecondary" to="/creer">Créer Liste</router-link></p>
    </div>
    <div class="imgAddListe">
      <img class="" src="/img/imgApp/liste-de-courses.png">
    </div>
  </div>
</div>

</div>

</template>

<script>
export default {
  name: 'accueil',
  data: function () {
    const listes = localStorage.getItem('listes')
    const donnees = JSON.parse(listes)
    return {
      donnees: donnees
    }
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

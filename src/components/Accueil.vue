<template>
<div>
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
    <h2 class="lightText">Créez votre liste d'épicerie en ligne</h2>
    <div class="addListeSecG">
      <p class="texteAddList lightText">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
      </p>
      <p><router-link class="btnSecondary" to="/creer">Créez votre Liste</router-link></p>
    </div>
    <div class="imgAddListe">
      <img class="" src="/img/imgApp/liste-de-courses.svg" alt="image liste">
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
  }
}
</script>

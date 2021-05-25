<template>
<div>
    <router-link to="/creer">Créer Liste</router-link>
    <h2>Listes</h2>
    <p v-for="(liste, index) in this.donnees" :key="index">
        <router-link :to="{ path: 'liste', query: { id: index }}">
            {{liste.nom}}
        </router-link>
    </p>
    <p><router-link to="/voir-tous">Voir tous les produits</router-link></p>
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

<style>

</style>

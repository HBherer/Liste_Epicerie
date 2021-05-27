<template>
  <div>
    <div>
      <h2>Voici tout les items qui sont disponible</h2>
      <p>Nombre de produits : {{produits.length}}</p>
      <div id="produits">
        <p v-for="(produits, index) in produits" :key="index">{{produits.nom}} {{produits.prix}} $
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
  }
}
</script>

<style>

</style>

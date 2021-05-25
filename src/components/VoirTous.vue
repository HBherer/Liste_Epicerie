<template>
<div>
    Nombre de produits : {{produits.length}}
     <div id="produits">
    <p v-for="(produits, index) in produits" :key="index">{{produits.nom}} - {{produits.prix}} $
    </p>
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

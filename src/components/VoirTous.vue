<template>
  <div>
    <div class="entete lightText">
      <div class="textFruitAll">
        <h2 class="countH">Voici tout les items qui sont disponible</h2>
        <p>Nombre de produits différent: {{produits.length}}</p>
      </div>
      <div class="groupImgFruit">
        <img class="fruitImg" src="/img/imgApp/fruit-du-dragon.png">
        <img class="fruitImg" src="/img/imgApp/pasteque.png">
        <img class="fruitImg" src="/img/imgApp/des-fruits(1).png">
        <img class="fruitImg del" src="/img/imgApp/kiwi.png">
        <img class="fruitImg" src="/img/imgApp/poire.png">
      </div>
    </div>
    <div>
      <div id="produits">
        <div class="itemAll" v-for="(produits, index) in produits" :key="index">
          <p class="p1">{{produits.nom}}</p>
          <img class="etiqette" src="/img/imgApp/marque.png">
          <p class="p2">Prix: {{produits.prix}}$</p>
        </div>
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

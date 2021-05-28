<template>
  <div>
    <div class="entete lightText">
      <div class="textFruitAll">
        <h2 class="countH">Voici tout les items qui sont disponible</h2>
        <p>Nombre de produits différent: {{produits.length}}</p>
      </div>
      <div class="groupImgFruit">
        <img class="fruitImg" src="/img/imgApp/fruit-du-dragon.svg" alt="image fruit-du-dragon">
        <img class="fruitImg" src="/img/imgApp/pasteque.svg" alt="image pasteque">
        <img class="fruitImg" src="/img/imgApp/des-fruits.svg" alt="image fruits">
        <img class="fruitImg del" src="/img/imgApp/kiwi.svg" alt="image kiwi">
        <img class="fruitImg" src="/img/imgApp/poire.svg" alt="image poire">
      </div>
    </div>
    <div>
      <div id="produits">
        <div class="itemAll" v-for="(produits, index) in produits" :key="index">
          <p class="p1">{{produits.nom}}</p>
          <img class="etiqette" src="/img/imgApp/marque.svg" alt="image marque">
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

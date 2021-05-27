<template>
<div>
  <div class="displayFlex">
    <div class="creatList lightText">
      <h2>Nouvelle liste d'épicerie</h2>
      <div class="creatListArea">
        <label class="h3" for="creatList">Entrez le nom de votre nouvelle liste</label>
        <input class="enterNameList" id="creatList" name="creatList" type="text" v-model="nom"/>
        <button class="btnSecondary" type="submit" @click=creerListe>Créer</button>
      </div>
      <div class="imgCreatListe">
        <img class="" src="/img/imgApp/document.png">
      </div>
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
    }
  }
}
</script>

<style>

</style>

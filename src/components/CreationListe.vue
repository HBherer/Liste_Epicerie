<template>
<div>
  <div class="displayFlex">
    <div class="creatList lightText">
      <h2>Nouvelle liste d'épicerie</h2>
      <div class="creatListArea">
        <form id="mon-form">
          <p class="errorRed" v-for="(erreur, index) in erreurs" :key="index">{{erreur}}</p>
          <label class="h3" for="creatList">Entrez le nom de votre nouvelle liste</label>
          <input class="enterNameList" id="creatList" name="creatList" type="text" v-model="nom"/>
          <button class="btnSecondary" type="submit" @click=creerListe>Créer</button>
        </form>
      </div>
      <div class="imgCreatListe">
        <img class="" src="/img/imgApp/document.svg" alt="image">
      </div>
    </div>
  </div>
</div>
</template>

<script>

export default {
  name: 'creerListe',
  data: function () {
    return { erreurs: [], nom: '' }
  },
  methods: {
    checkForm: function (e) {
      this.erreurs = []
      if (this.nom === '') {
        this.erreurs.push('Le nom est requis')
      }
      if (this.erreurs.length > 0) {
        e.preventDefault()
      } else {
        this.creerListe()
      }
    },
    creerListe: function () {
      if (!this.nom) {
        this.erreurs = ['Vous devez entrez un nom de liste']
      } else {
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
        this.$router.push({ path: '/liste', query: { id: id, allo: 'aaa' } })
      }
    }

  }
}
</script>

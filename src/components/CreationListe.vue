<template>
<div>
    <input type="text" v-model="nom"/>
    <button type="submit" @click=creerListe>Créer</button>
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

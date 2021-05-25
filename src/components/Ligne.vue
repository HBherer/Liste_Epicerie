<template>
<div>
    <p>{{this.nom}}</p>
    <p  v-if="this.editable" @click=retrait()>Retrait</p>
    <p>{{this.qte}}</p>
    <p v-if="this.editable"  @click=ajout()>Ajout</p>
    <p >{{totalLigne}}</p>
</div>
</template>

<script>
export default {
  name: 'ligne',
  data: function () {
    console.log(this.editable)
    return {
      qte: 1
    }
  },
  props: ['id', 'nom', 'prix', 'editable'],
  methods: {
    ajout: function () {
      this.qte += 1
      this.$emit('maj', this.id, this.qte)
    },
    retrait: function () {
      this.qte -= 1
      this.$emit('maj', this.id, this.qte)
    }
  },
  computed: {
    totalLigne: function () {
      return this.qte * this.prix
    }
  }
}
</script>

<style>

</style>

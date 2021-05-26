<template>
<div class="items">
    <p class="nomItem">{{this.nom}}</p>
    <p class="AddRemoveItemToListe"  v-if="this.editable" @click=retrait()>-</p>
    <p class="qteItem">{{this.qte}}</p>
    <p class="AddRemoveItemToListe" v-if="this.editable"  @click=ajout()>+</p>
    <p class="prixItem">Total: {{totalLigne}} $</p>
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
.items{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  border: solid 2px #2c3e50;
  margin: 15px;
  border-radius: 12px;
}
.nomItem{
  text-align: center;
  color: #2c3e50;
  font-family: 'Open Sans', sans-serif;
  font-weight: 700;
  font-size: 1.3rem;
  margin-bottom: 5px;
  width: 100%;
}
.AddRemoveItemToListe{
  color: #ffffff;
  font-family: 'Open Sans', sans-serif;
  font-weight: 700;
  font-size: 1.8rem;
  cursor: pointer;
  padding: 0px 15px;
  height: auto;
  border-radius: 12px;
  background-color: #058373;
}
.qteItem{
  color: #2c3e50;
  font-family: 'Open Sans', sans-serif;
  font-weight: 700;
  font-size: 1.2rem;
  margin: 5px;
}
.prixItem{
  width: 100%;
  color: #2c3e50;
  font-family: 'Open Sans', sans-serif;
  font-weight: 700;
  text-align: center;
}
</style>

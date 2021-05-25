import Vue from 'vue'
import Router from 'vue-router'
import Accueil from '../components/Accueil.vue'
import Liste from '../components/Liste.vue'
import CreationListe from '../components/CreationListe.vue'
import VoirTous from '../components/VoirTous.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Accueil',
      component: Accueil
    },
    {
      path: '/creer',
      name: 'Création de liste',
      component: CreationListe
    },
    {
      path: '/liste',
      name: 'Liste',
      component: Liste
    },
    {
      path: '/voir-tous',
      name: 'Voir tous',
      component: VoirTous
    }
  ]
})

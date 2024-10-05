import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Record from '../views/Record.vue'
import Content from '../views/Content.vue'
import Quiz from '../views/Quiz.vue'
import Quiz2 from '../views/Quiz2.vue'
import Cards from '../views/Cards.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: Home },
    { path: '/record', name: 'record', component: Record },
    { path: '/content', name: 'content', component: Content },
    { path: '/quiz', name: 'quiz', component: Quiz },
    { path: '/quiz2', name: 'quiz2', component: Quiz2 },
    { path: '/cards', name: 'cards', component: Cards },
  ]
})

export default router

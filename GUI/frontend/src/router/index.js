import HomePage from './../components/HomePage.vue'
import TextDisplay from './../components/TextDisplay.vue'
import {createRouter, createWebHistory} from 'vue-router'


const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', name: "HomePage", component: HomePage, props: true },
        { path: '/display', name: "TextDisplay", component: TextDisplay, props: true},
      ]
});

export default router;

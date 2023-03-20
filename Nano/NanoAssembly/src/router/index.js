import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/AboutView.vue')
    },
    {
        path: '/seq',
        name: 'seq',
        component: () =>
            import ('../views/Seq/SeqView.vue')
    },
    {
        path: '/seqcirc',
        name: 'seq_circ',
        component: () =>
            import ('../views/Seq/SeqCircView.vue')
    },
    {
        path: '/seqline',
        name: 'seq_line',
        component: () =>
            import ('../views/Seq/SeqLineView.vue')
    },
]

const router = new VueRouter({
    routes
})

export default router
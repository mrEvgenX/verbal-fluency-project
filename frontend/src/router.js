import Vue from 'vue'
import Router from 'vue-router'
import App from './components/App.vue'
import TotalScore from './components/TotalScore.vue'
import Profile from './components/Profile.vue'
import Login from './components/Login.vue'
import Register from './components/Register.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: App
        }, {
            path: '/login',
            component: Login
        }, {
            path: '/register',
            component: Register
        }, {
            path: '/profile',
            component: Profile
        }, {
            path: '/profile/total_score',
            component: TotalScore
        }
    ]
});

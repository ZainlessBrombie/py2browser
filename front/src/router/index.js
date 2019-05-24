import Vue from 'vue'
import Router from 'vue-router'
import Main from "../pages/Main";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Py2Browser',
      component: Main,
    }
  ]
})

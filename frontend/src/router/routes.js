
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/', component: () => import('pages/Login.vue')},
      { path: '/index', component: () => import('pages/Index.vue') },
      { path: '/reg', component: () => import('pages/Register.vue')},
      { path: '/foods', component: () => import('pages/Foods.vue')},
      { path: '/search', component: () => import('pages/Search.vue')},
      { path: '/detail', name: 'detail', component: () => import('pages/Detail.vue')}
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes

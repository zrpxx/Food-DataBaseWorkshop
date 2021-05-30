<template>
  <q-layout view="hHh lpR lFf">

    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="left = !left" v-if="loggedIn" />

        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">
          </q-avatar>
          Foods
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="left" side="left" elevated v-if="loggedIn">
      <q-item v-ripple exact to="/index">
        <q-item-section avatar>
          <q-icon name="dashboard"/>
        </q-item-section>
        <q-item-section>
          <q-item-label>Home</q-item-label>
        </q-item-section>
      </q-item>

        <q-item v-ripple exact to="/foods">
          <q-item-section avatar>
            <q-icon name="list"/>
          </q-item-section>
          <q-item-section>
            <q-item-label>Foods</q-item-label>
          </q-item-section>
        </q-item>

      <q-item v-ripple exact to="/search">
        <q-item-section avatar>
          <q-icon name="search"/>
        </q-item-section>
        <q-item-section>
          <q-item-label>Search</q-item-label>
        </q-item-section>
      </q-item>

      <q-item v-ripple exact to="/detail">
        <q-item-section avatar>
          <q-icon name="analytics"/>
        </q-item-section>
        <q-item-section>
          <q-item-label>Info</q-item-label>
        </q-item-section>
      </q-item>

      <q-item v-ripple clickable @click="onLogout()">
        <q-item-section avatar>
          <q-icon name="logout"/>
        </q-item-section>
        <q-item-section>
          <q-item-label>Log out</q-item-label>
        </q-item-section>
      </q-item>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer bordered class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <a class="text-h6 float-left" style="font-size: 16px">Made with 💗&nbsp;&nbsp;By 胡逸(1930026045), 谷恺琦(1930026035), 胡惟聪(1930026044) & 王瀚锋(1930026116).</a>
          <a class="text-h6 float-right">Version: <q-badge color="primary">{{ version }}</q-badge></a>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script>
export default {
  data () {
    return {
      left: false,
      version: "V0.2.2",
      loggedIn: false
    }
  },
  created() {
    this.loggedIn = sessionStorage.getItem('loggedIn') !== null
    const timer = setInterval(() => {
      this.checkLogin();//你所加载数据的方法

    }, 500)
  },
  methods: {
    onLogout() {
      console.log('logout')
      sessionStorage.removeItem('loggedIn')
      sessionStorage.removeItem('role')
      this.loggedIn = false
      this.$router.replace('/')
    },
    checkLogin() {
      this.loggedIn = sessionStorage.getItem('loggedIn') !== null
      if(this.loggedIn) {
        if(this.$route.path === '/')
          this.$router.push('/index')
      }
      else {
        if(this.$route.path !== '/' && this.$route.path !== '/reg')
          this.$router.push('/')
      }
    }
  }
}
</script>

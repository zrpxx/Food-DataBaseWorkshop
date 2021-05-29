<template>
  <q-layout view="hHh lpR lFf">

    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="left = !left" />

        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">
          </q-avatar>
          Foods
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="left" side="left" elevated>
        <q-item v-ripple exact to="/index">Index</q-item>
        <q-item v-ripple>Logout</q-item>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer bordered class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <a class="text-h6 float-left" style="font-size: 14px">Created with 💗 By 胡逸(1930026045), 谷恺琦(1930026035), 胡惟聪(1930026044) & 王瀚锋(1930026116).</a>
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
      version: "V0.2.2"
    }
  }
}
</script>

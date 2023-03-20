<template>
  <v-app>
    <v-app-bar app>
      <router-link
        to="/"
        class="v-toolbar__content"
        style="text-decoration: none; color: black"
      >
        <div style="max-width: 216px" class="mr-3">
          <v-img to="/" :src="require('@/assets/Nano_Logo.png')"></v-img>
        </div>
        <span class="text-h5" style="white-space: nowrap"> NanoAssembly for Primer Design </span>
      </router-link>

      <v-tabs v-model="tab" left>
        <v-tab v-for="page in pages" :key="page.tab" :to="page.to">
          {{ page.tab }}
        </v-tab>
      </v-tabs>
    </v-app-bar>

    <v-main>
      <v-container fluid class="pa-0">
        <router-view />
      </v-container>
    </v-main>
    <v-footer dark padless>
      <v-card flat tile class="info white--text text-center grow">

        <v-card-text class="white--text">
          {{ new Date().getFullYear() }} —
          <strong>清华大学生命学院</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script></script>

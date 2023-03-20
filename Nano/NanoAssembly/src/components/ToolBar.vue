<template>
  <v-app-bar app color="info">
    <router-link
      to="/"
      class="v-toolbar__content"
      style="text-decoration: none; color: white"
    >
      <div style="max-width: 54px" class="mr-3">
        <v-img to="/" :src="require('@/assets/cfjd_logo.png')"></v-img>
      </div>
      <div class="text-h5">南京传锋机电科技有限公司</div>
    </router-link>

    <v-spacer></v-spacer>

    <v-btn to="/" plain>主页</v-btn>
    <v-btn to="/product/" plain>产品</v-btn>
    <v-btn to="/info/" plain>新闻</v-btn>
    <v-btn to="/contact/" plain>联系我们</v-btn>
    <v-tooltip bottom>
      <template v-slot:activator="{ on, attrs }">
        <v-btn to="/login/" icon v-bind="attrs" v-on="on">
          <v-icon>mdi-login</v-icon>
        </v-btn>
      </template>
      <span>{{ user ? "切换用户" : "登录" }}</span>
    </v-tooltip>

    <!-- <v-tooltip bottom v-if="user">
        <template v-slot:activator="{ on, attrs }">
          <v-btn to="/profile/" icon v-bind="attrs" v-on="on">
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </template>
        <span>用户信息</span>
      </v-tooltip> -->
  </v-app-bar>
</template>

<script>
export default {
  name: "ToolBar",
  computed: {
    user() {
      return this.$store.state.user;
    },
  },
};
</script>
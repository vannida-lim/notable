<template>
  <v-app>
    <v-main>
      <Physicians />
    </v-main>
  </v-app>
</template>

<script>
import Physicians from './components/Physicians';

export default {
  name: 'App',

  components: {
    Physicians ,
  },

  data: () => ({
    //
  }),
};
</script>

<template>
  <div>
    <h1>Notable</h1>
      <h2>Physicians</h2>
      <div
          v-for="(physician, i) in physicians"
          :key="i"
        >
        <div @click="showAppointments(physician)">{{ formatName(physician.name) }}</div>
    </div>
    <div v-if="visibileAppointments">
      <h2>Dr. {{ selectedDoc }}</h2>
      <h3>{{ selectedDocEmail }}</h3>
      <v-data-table
        :headers="headers"
        :items="appointments">
      </v-data-table>
    </div>

    <button>Logout</button>
  </div>
</template>

<script>
export default {
  data: () => ({
    selected: 1,
    physicians: [],
    visibileAppointments: false,
    headers: [
      { text: '#', value: 'id'}, 
      { text: 'Name', value: 'name'}, 
      { text:'Time', value: 'time'}, 
      { text: 'Kind', value: 'kind'},
    ],
    appointments: [],
    selectedDoc: '',
    selectedDocEmail: '',
  }),

  created() {
      fetch('http://127.0.0.1:5000/physicians', 
      { headers: {
        "Access-Control-Allow-Origin": "*",
      }}).then(r => r.json()).then(data => { this.physicians = data})
  },

  methods: {
    showAppointments(physician) {
      this.visibileAppointments = true
      this.selectedDoc = physician.name
      this.selectedDocEmail = physician.email
      this.appointments = physician.appointments
    },

    formatName(name) {
      let first = name.split(' ')[0]
      let last = name.split(' ')[1]
      return `○ ${last}, ${first}`
    }
  }
  
}
</script>

<style scoped>
div {
  margin: 5px;
}

button {
  background-color: blue;
  color: white;
  border-radius: 3px;
}
</style>

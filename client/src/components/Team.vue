<template>
  <div class="team">
    <h1 class="subtitle-1 grey--text mx-4">
      Team
    </h1>

    <v-container class="my-5">
      <v-row
        row
        wrap
      >
        <v-col
          v-for="person in team"
          :key="person.name"
          cols="12"
          xs="12"
          sm="6"
          md="4"
          lg="3"
        >
          <v-card
            flat
            class="text-center"
          >
            <v-responsive class="pt-4">
              <!-- <v-img :src="person.img_src">
              </v-img> -->
              <v-avatar
                class="grey lighten-4"
                size="100"
              >
                <img :src="person.img_src">
              </v-avatar>
            </v-responsive>
            <v-card-text>
              <div class="subtitle-1">
                {{ person.name }}
              </div>
              <div class="grey--text">
                {{ person.role }}
              </div>
            </v-card-text>
            <v-card-actions class="justify-center">
              <v-btn
                text
                color="grey"
              >
                <v-icon
                  small
                  left
                >
                  mdi-message
                </v-icon>
                <span>Message </span>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>

export default {
  data () {
    return {
      team: [
        { name: "Rohi Zalcman", role: "Web developer", img_src: "https://scontent.ftlv1-2.fna.fbcdn.net/v/t1.0-1/p160x160/13501757_10206043711118218_1400724738522122616_n.jpg?_nc_cat=103&_nc_sid=dbb9e7&_nc_oc=AQkYOdKcQiSPp0hv3MDr9bigvt5FsVmPAV5Ab26TRnZ4IpR9V8FtxcvtUddplAiUkYWDHbRB9yKK6WUNLHQIBB1Q&_nc_ht=scontent.ftlv1-2.fna&_nc_tp=6&oh=13d4bd6554c1d249c0c119a8e1243cc1&oe=5ED03D38" },
        { name: "Oren Keller", role: "Python programmer", img_src: "https://scontent.ftlv1-2.fna.fbcdn.net/v/t1.0-1/p160x160/11896167_10206447037347315_8282216349495566933_n.jpg?_nc_cat=103&_nc_sid=dbb9e7&_nc_oc=AQk99rGjnSlEfmXxtJenAENAWi4djgbkqmpqEjM2t2q_AbXMarQPR9ptx6O71Qt02iQT68fv4q5FildLZa-4xNpn&_nc_ht=scontent.ftlv1-2.fna&_nc_tp=6&oh=f78b7e65534b0f511b832ed9e05851c2&oe=5ECF9176" },
        { name: "Imri Luzzattov", role: "Unemployed", img_src: "https://scontent.ftlv1-1.fna.fbcdn.net/v/t1.0-1/p160x160/46076572_10217495631008349_5490987805284761600_n.jpg?_nc_cat=100&_nc_sid=dbb9e7&_nc_oc=AQlY7_Yy8WYsT0VCd59GxBrTCXiGkNf_MYvu5uWW9aaSAIFHcPfTTJC57AwUNqQg_IXcb7etZjL-l17-_EM9cD2I&_nc_ht=scontent.ftlv1-1.fna&_nc_tp=6&oh=74071d10c3f85c6e7ce24ecda0c6092f&oe=5ECF538F" }
      ]
    };
  },
};
</script>

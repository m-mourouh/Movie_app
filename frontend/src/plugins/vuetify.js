// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'

const myCustomLightTheme = {
  colors: {
    "grey-5": "#212426",
    "grey-4": "#343739",
    "grey-3": "#6F6F6F",
    white: "#FFFFFF",
  },
};


export default createVuetify({
  theme: {
    defaultTheme: "myCustomLightTheme",
    themes: {
      myCustomLightTheme,
    },
  },
});

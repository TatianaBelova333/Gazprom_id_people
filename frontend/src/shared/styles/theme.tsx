// import { ThemeConfig } from "antd/es/config-provider/context";

const theme = {
  token: {
    fontFamily: "Roboto, Segoe UI, Arial, sans-serif",
    fontSizeHeading1: 24,
    // lineHeightHeading1: 32,
    fontWeightHeading1: 500,
    // padding: 0,
    // margin: 0,

    fontSizeHeading2: 20,
    lineHeightHeading2: 24,
    fontWeightHeading2: 500,

    fontSizeHeading3: 16,
    lineHeightHeading3: 20,
    fontWeightHeading3: 400,

    // fontSizeHeading4: 12,
    // lineHeightHeading4: 12,

    // fontSizeHeading5: 12,
    // lineHeightHeading5: 12,

    fontSizeLG: 12,
    lineHeightLG: 12,

    fontSizeSM: 12,
    lineHeightSM: 12,

    colorPrimary: "rgba(9, 109, 217, 1)",
    borderRadius: 2,
  },

  components: {
    Checkbox: {
    },
    Button: {
      colorPrimary: "rgba(9, 109, 217, 1)",
      // borderColorDisabled: 'transparent', // Убираем обводку у кнопок в состоянии disabled
      contentFontSize: 14, // Размер шрифта для кнопок по умолчанию
    },
  },
};

export default theme;


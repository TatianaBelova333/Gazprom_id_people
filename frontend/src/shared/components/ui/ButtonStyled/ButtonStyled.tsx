// import { useState } from 'react'
import {
  Button,
} from "antd";
import styled from "styled-components";



const ButtonStyled = styled(Button)`

  font-size: 16px;
  font-weight: 400;
  /* Основные стили для кнопки primary */
  &.ant-btn-primary {
    background-color: rgba(9, 109, 217, 1);
    color: #fff;
    
    /* Стили для состояния hover */
    &:hover {
      background-color: rgba(7, 92, 184, 1);
    }

    /* Стили для состояния disabled */
    &:disabled {
      background-color: rgba(27, 44, 78, 0.05);
      border-color: transparent;
      color: rgba(27, 44, 78, 0.2);
    }
  }

  /* Стили для кнопки default */
  &.ant-btn-default {
    background-color: #ffffff;

    /* Стили для состояния hover */
    &:hover {
      background-color: #f5f5f5;
      border-color: #d9d9d9;
      color: rgba(0, 0, 0, 0.88);
    }
  }

  /* Стили для кнопки типа text */
  &.ant-btn-text {
    background-color: transparent;
    border: none;
    color: rgba(24, 144, 255, 1);
    height: 56px;

    /* Стили для состояния hover */
    &:hover {
      background-color: rgba(0, 0, 0, 0.06);
      color: rgba(0, 0, 0, 0.88);
    }

    /* Стили для состояния disabled */
    &:disabled {
      background-color: transparent;
      color: rgba(0, 0, 0, 0.25);
    }
  }
`;

export default ButtonStyled;
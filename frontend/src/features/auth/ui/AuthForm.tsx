import { useState } from "react";
import { Form, Input, Tabs, Typography } from "antd";
import styled from "styled-components";
import Button from "../../../shared/components/ui/ButtonStyled";

const { Title } = Typography;

const FormContainer = styled.div`
  width: 360px;
`;

const ButtonWithSize = styled(Button)`
  width: 360px;
  height: 56px;
  margin: 12px 0 -10px;
`;

const StyledTabs = styled(Tabs)`
  .ant-tabs-nav-list {
    width: 296px;
    display: flex;
    justify-content: space-between;
    margin-right: "20px";
  }

  .ant-tabs-nav-wrap {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .ant-tabs-tab {
    width: 50%;
    height: 55px;
    margin: 0 auto;
  }

  .ant-tabs-tab-btn {
    font-weight: 400;
    font-size: 16px;
    line-height: 20px;
    text-align: center;
    margin: 0 auto;
  }
`;

const StyledTitle = styled(Title)`
  height: 49px;
  text-align: center;
`;

const StyledFormItem = styled(Form.Item)`
  width: 360px;
  margin-bottom: 20px;

  .ant-input,
  .ant-input-password {
    height: 64px;
    font-size: 16px;
  }

  .ant-input-affix-wrapper {
    height: 64px;
  }

  .ant-form-item-explain-error {
    font-weight: 400;
    font-size: 14px;
    line-height: 22px;
    text-align: left;
  }

`;

function AuthForm() {
  const [loading, setLoading] = useState(false);

  function onClickButton() {
    console.log("button clicked");
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
    }, 2000);
  }

  const tabItems = [
    {
      key: "1",
      label: "Вход",
      children: (
        <>
          <StyledTitle>Вход в личный кабинет</StyledTitle>
          <Form
            style={{
              width: "100%",
            }}
            name="login"
            initialValues={{ remember: true }}
            autoComplete="off"
          >
            <StyledFormItem
              name="email"
              rules={[{ required: true, message: "Введите электронную почту" }]}
            >
              <Input placeholder="Введите электронную почту" />
            </StyledFormItem>

            <StyledFormItem
              name="password"
              rules={[{ required: true, message: "Введите пароль" }]}
            >
              <Input.Password placeholder="Введите пароль" />
            </StyledFormItem>

            <Form.Item>
              <ButtonWithSize
                type="primary"
                htmlType="submit"
                block
                loading={loading}
                onClick={onClickButton}
              >
                Войти
              </ButtonWithSize>
            </Form.Item>

            <Form.Item>
              <Button type="link">Не помню пароль</Button>
            </Form.Item>
          </Form>
        </>
      ),
    },
    {
      key: "2",
      label: "Регистрация",
      children: (
        <>
          <StyledTitle>Вход в личный кабинет</StyledTitle>
          <Form
            style={{
              width: "100%",
            }}
            name="login"
            initialValues={{ remember: true }}
            autoComplete="off"
          >
            <StyledFormItem
              name="email"
              rules={[{ required: true, message: "Введите электронную почту" }]}
            >
              <Input placeholder="Введите электронную почту" />
            </StyledFormItem>

            <StyledFormItem
              name="password"
              rules={[{ required: true, message: "Введите код" }]}
            >
              <Input.Password placeholder="Введите код" />
            </StyledFormItem>

            <Form.Item>
              <ButtonWithSize
                type="primary"
                htmlType="submit"
                block
                loading={loading}
                onClick={onClickButton}
              >
                Далее
              </ButtonWithSize>
            </Form.Item>

          </Form>
        </>
      ),
    },
  ];

  return (
    <FormContainer>
      <StyledTabs defaultActiveKey="1" items={tabItems} />
    </FormContainer>
  );
}

export default AuthForm;
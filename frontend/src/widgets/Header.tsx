import { Layout, Avatar } from "antd";
import { BellOutlined, QuestionCircleOutlined } from "@ant-design/icons";
import styled from "styled-components";
import LogoImage from "../shared/components/ui/LogoImage/LogoImage";
// import QuestionCircleOutlined from "@ant-design/icons";
import Bell from "../shared/components/ui/Bell/Bell";

// const { Header } = Layout;

const StyledHeader = styled(Layout.Header)`
  height: 80px;
  flex-grow: 1;
  padding: 0;
`;

const BoundingBox = styled.div`
  max-width: 1440px;
  display: flex;
  column-gap: 40px;
  justify-content: space-between;
  align-items: center;
`;

const WelcomeTextContainer = styled.div`
  flex-grow: 1; /* Заполняет всё свободное пространство */
  /* display: flex;
  align-items: center; */
`;

const WelcomeText = styled.h1`
  margin: 0;
  font-size: 24px;
  text-align: left;
  /* color: var(--main-blue); */
`;

const UserSection = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 226px;
`;

const Notifications = styled(BellOutlined)`
  font-size: 24px;
  margin-right: 16px;
`;

const HelpIcon = styled(QuestionCircleOutlined)`
  font-size: 24px;
  margin-right: 16px;
`;

const UserName = styled.span`
  font-size: 16px;
  margin-left: 8px;
`;

const LogoBackground = styled.div`
  width: 207px;
  height: 80px;
  background-color: white;
`;

const HeaderMainBlock = styled.div`
  width: 100%;
  height: 100%;
`;

const Header = () => {
  return (
    <StyledHeader
      style={{
        background: "var(--light-blue)",
      }}
    >
      <BoundingBox>
        <LogoBackground>
          <LogoImage alt="Газпром People ID" />
        </LogoBackground>
        <WelcomeTextContainer>
          <WelcomeText>Добро пожаловать, Александр!</WelcomeText>
        </WelcomeTextContainer>
        <UserSection>
          <QuestionCircleOutlined />
          <Bell notifications={10} />
          <Avatar src="https://path_to_user_photo.png" />
          <UserName>Александр</UserName>
        </UserSection>
      </BoundingBox>
    </StyledHeader>
  );
};

export default Header;

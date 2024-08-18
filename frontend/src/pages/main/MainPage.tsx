import { 
  Layout, 
  // Menu, 
  // Avatar,
} from 'antd';
import styled from 'styled-components';
import Header from '../../widgets/Header';
import MenuMain from '../../shared/components/ui/Menu';
import Button from '../../shared/components/ui/ButtonStyled';
import ProjectDescription from '../../widgets/ProjectCard';

const { Sider, Content } = Layout;

const AppLayout = styled(Layout)`
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100vh;
  overflow: scroll;
  background: var(--light-blue);
`;

const StyledContent = styled(Content)`
  max-width: 618px;
  min-width: 360px;
  margin: 0 40px;
  position: relative;
  flex-grow: 1;

  @media (max-width: 768px) {
    width: 100%;
    margin: 0;
  }
`;

const RightColumn = styled.div`
  max-width: 532px;
  min-width: 360px;
  margin-left: 16px;
  flex-grow: 1;

  @media (max-width: 768px) {
    width: 100%;
    margin: 0;
  }
`;

const ButtonStyled = styled(Button)`
  margin-top: auto;
`;

const BoundingBox = styled.div`
  max-width: 1440px;
  display: flex;
  /* column-gap: 40px; */
  /* justify-content: space-between; */
  align-items: center;
`;

const MainPage = () => {
  return (
    <AppLayout>
      <Header />
      <Layout
        style={{
          background: 'var(--light-blue)',
          flexWrap: 'wrap',
          overflow: 'scroll',
          flexGrow: 1,
        }}
      >
        <Sider
          theme='light'
          width={207}
          // flexGrow=1,
        >
          <MenuMain />
          <ButtonStyled style={{ bottom: '24px', left: '24px', position: 'absolute' }}>
            Выйти из системы
          </ButtonStyled>
        </Sider>

        <StyledContent>
          <ProjectDescription />
          <ProjectDescription />
        </StyledContent>

        <RightColumn>
          <p>drtg</p>
        </RightColumn>
      </Layout>
    </AppLayout>
  );
};

export default MainPage;

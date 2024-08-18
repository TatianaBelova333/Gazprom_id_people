
//todo , шрифты подключить, проверить мусор, написать ридми, настроить линтер

import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import styled from "styled-components";
import {
  ConfigProvider,
  // DatePicker,
} from "antd";
import theme from "../shared/styles/theme";
import MainPage from "../pages/main/MainPage";
import AuthPage from "../pages/auth/AuthPage";
// import ProjectsPage from "../pages/projects/ProjectsPage"; // страница проектов

const StyledMain = styled.main`
  overflow: auto;
  overflow-y: scroll;
`;

const ProtectedRoute: React.FC<{
  isLoggedIn: boolean;
  children: React.ReactNode;
}> = ({ isLoggedIn, children }) => {
  return isLoggedIn ? <>{children}</> : <Navigate to="/auth" />;
};

function App() {
  const [isLoggedIn, setIsLoggedIn] = React.useState(true);

  return (
    <ConfigProvider theme={theme}>
      <StyledMain>
        <Router>
          <Routes>
            {/* Защищенный маршрут для главной страницы */}
            <Route
              path="/"
              element={
                <ProtectedRoute isLoggedIn={isLoggedIn}>
                  <MainPage />
                </ProtectedRoute>
              }
            />
            {/* Защищенный маршрут для страницы проектов */}
            {/* <Route
              path="/projects"
              element={
                <ProtectedRoute isLoggedIn={isLoggedIn}>
                  <ProjectsPage />
                </ProtectedRoute>
              }
            /> */}
            {/* Маршрут для страницы авторизации */}
            <Route
              path="/auth"
              element={<AuthPage setIsLoggedIn={setIsLoggedIn} />}
            />
            {/* Маршрут для страницы 404 */}
            <Route path="*" element={<div>404 - Page Not Found</div>} />
          </Routes>
        </Router>
        {/* Готовые компоненты */}
        {/* <CascadingMenu /> */}
        {/* <DatePicker />
        {/* <GiftOutlined /> */}
        {/* Готовые компоненты */}
      </StyledMain>
    </ConfigProvider>
  );
}

export default App;

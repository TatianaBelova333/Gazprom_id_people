import {
  Tabs,
} from "antd";

import styled from "styled-components";

import {
  UnorderedListOutlined,
  PartitionOutlined,
  ProjectOutlined,
  AppstoreOutlined,
} from "@ant-design/icons";

const menuItems = [
  {
    key: "1",
    icon: <AppstoreOutlined />,
    label: "Главная",
    content: "Content for Структура компании", //
  },
  {
    key: "2",
    icon: <UnorderedListOutlined />,
    label: "Справочник",
    content: "Content for Структура компании", //
  },
  {
    key: "3",
    icon: <ProjectOutlined />,
    label: "Проекты",
    content: "Content for Структура компании", //
  },
  {
    key: "4",
    icon: <PartitionOutlined />,
    label: "Структура компании",
    content: "Content for Структура компании",
  },
];

const { TabPane } = Tabs;

const StyledTab=styled(TabPane)`
  padding: 0 0 300px; 
  margin: 0 0 300px;
  gap: 300px;
`;

function MenuMain() {
  return (
    <>
      <div style={{ display: "flex", padding: "7vh 0 0" }}>
        <Tabs
          // activeKey={selectedKey}
          // onChange={handleTabChange}
          tabPosition="left"
          tabBarStyle={{ padding: "12px 0", textAlign: "center" }}
        >
          {menuItems.map((item) => (
            <StyledTab tab={item.label} key={item.key} icon={item.icon}></StyledTab>
          ))}
        </Tabs>
      </div>
    </>
  );
}

export default MenuMain;

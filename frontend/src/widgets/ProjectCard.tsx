import styled from "styled-components";
import { Card, Typography, Avatar, Row, Col } from "antd";
import TagCloud from "../shared/components/ui/Tags";

const { Title, Text } = Typography;
const Flex = styled.div`
  display: flex;
  gap: 12px;
  flex-direction: column;
`;

const StyledCard = styled(Card)`
  width: 618;
  height: auto;
  border-radius: 2;
  border: 1px solid #d9d9d9;
  margin: 16px 0;
`;

const ProjectDescription = () => {
  return (
    <StyledCard
    >
      {/* Первый контейнер */}
      <div>
        <Title
          level={2}
          style={{
            fontWeight: 500,
            fontSize: 20,
            lineHeight: "24px",
            textAlign: "left",
          }}
        >
          Сервис Газпром ID People
        </Title>
        <Typography
          style={{
            fontSize: 14,
            lineHeight: "22px",
            fontWeight: 400,
            textAlign: "left",
          }}
        >
          Программное обеспечение для построения организационных диаграмм,
          разработанное для того, чтобы помочь компаниям управлять своей
          организационной структурой и визуализировать ее. Проект состоит из
          четырех разделов. Первый - справочник сотрудников компании. Второй -
          раздел с проектами. На этой странице реализована возможность
          перемещать сотрудников или целые отделы между проектами. Третий раздел
          посвящен структуре компании. Она представлена в виде дерева, которое
          автоматически генерируется на основе базы сотрудников. Последний
          раздел - это главная страница, на которой сотрудник может
          просматривать свои проекты и сохраненные контакты коллег.
        </Typography>
        <div style={{ marginTop: 16 }}>
          <TagCloud />
        </div>
      </div>

      {/* Разделение между блоками */}
      <div style={{ height: 28 }} />

      {/* Второй контейнер */}
      <div style={{ padding: 16 }}>
        <Title
          level={3}
          style={{
            fontWeight: 400,
            fontSize: 16,
            lineHeight: "24px",
            textAlign: "left",
          }}
        >
          Команда проекта
        </Title>
        <Row gutter={24} style={{ marginBottom: 16, height: 62 }}>
          <Row flex="1">
            <Avatar size={40} style={{ marginRight: -8 }} />
            <Flex>
              <Typography>Алексеева Анна</Typography>
              <Typography>Product Manager</Typography>
            </Flex>
          </Row>
          <Col flex="1">
            {/* Содержимое второго блока */}
            <Text>Участник 2</Text>
          </Col>
          <Col flex="1">
            {/* Содержимое третьего блока */}
            <Text>Участник 3</Text>
          </Col>
        </Row>
        <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
          <Avatar size={40} style={{ marginRight: -8 }} />
          <Avatar size={40} style={{ marginRight: -8 }} />
          <Avatar size={40} style={{ marginRight: -8 }} />
          <Avatar size={40} style={{ marginRight: -8 }} />
          <Avatar size={40} style={{ marginRight: -8 }} />
          <Avatar size={40} style={{ marginRight: -8 }} />
          <Avatar size={40} style={{ marginRight: -8 }} />
          <Avatar size={40} style={{ marginRight: -8 }} />
          <Avatar
            size={40}
            style={{ backgroundColor: "var(--main-blue)", marginRight: -8 }}
          >
            +2
          </Avatar>
        </div>
      </div>
    </StyledCard>
  );
};

export default ProjectDescription;

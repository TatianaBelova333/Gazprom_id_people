import {Tag} from 'antd';
import styled from "styled-components";

const tags = [
  { name: "В работе", color: "gold" },
  { name: "Внутренний продукт", color: "blue" },
  { name: "Веб-сервис", color: "blue" },
  { name: "Структура организации", color: "blue" },
  { name: "Хакатон", color: "blue" },
  { name: "Справочник сотрудников", color: "blue" },
  { name: "Проекты", color: "blue" },
  { name: "Контакты сотрудника", color: "blue" },
  { name: "MVP", color: "blue" },
];

const StyledTag = styled(Tag)`
  font-size: 14px;
  line-height: 2;
  margin: 4px;
  padding: 0 8px;
  border-radius: 2px;
  height: 28px;  
  border: none;
  /* Фикс для специфичных случаев, где цвет текста может быть переопределен */
  &.ant-tag {
    color: black;
  }
`;


function TagCloud() {
  return (
    <div>
    {tags.map((tag, index) => (
      <StyledTag
        key={index}
        color={tag.color}
        bordered={false}
      >
        {tag.name}
      </StyledTag>
    ))}
  </div>
  );
}

export default TagCloud;
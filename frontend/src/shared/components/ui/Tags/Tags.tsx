import {Tag} from 'antd';
import styled from "styled-components";
import { DataType } from "./types";

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

const Container = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: center;

`;

const TagCloud = ({ data }: { data: DataType }) => {
  if (!data || !data.tags || data.tags.length < 1) {
    return (
      <Container>
        <p>Ключевые слова не определены</p>
      </Container>
    );
  }

  return (
    <Container>
      {data.tags.map((tag) => (
        <StyledTag
          key={tag.id}
          color={tag.color}
          bordered={false}
        >
          {tag.name}
        </StyledTag>
      ))}
    </Container>
  );
}

export default TagCloud;
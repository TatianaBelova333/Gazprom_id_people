import {
  Badge,
} from "antd";

import {
  BellOutlined,
} from "@ant-design/icons";

function Bell({ notifications }: { notifications: number }) {
  return (
    <Badge
      count={notifications}
      offset={[0, 0]}
      style={{ backgroundColor: "#f5222d", color: "#fff" }}
    >
      <BellOutlined />
    </Badge>
  );
}

export default Bell;

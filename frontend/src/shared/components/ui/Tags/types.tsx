// Интерфейс для статуса
interface Status {
  id: number;
  name: string;
  color: string;
}

// Интерфейс для тегов
interface Tag {
  id: number;
  name: string;
  color: string;
}

// Интерфейс для участников команды
interface TeamMember {
  id: number;
  image: string;
}

// Интерфейс для директора
interface Director {
  id: number;
  full_name: string;
  position: string;
  phone_number: string;
  telegram: string;
  email: string;
  image: string;
  employment_type: number;
  ms_teams: string;
}

// Основной интерфейс для объекта
export interface DataType {
  id: number;
  name: string;
  description: string;
  status: Status;
  tags: Tag[];
  team_members: TeamMember;
  team_extra_count: number;
  director: Director;
}
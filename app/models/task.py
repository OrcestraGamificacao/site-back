from app.models.meta import Base
from sqlalchemy import Column, String, Integer, Boolean


class Task(Base):
    """
    Classes que herdam de 'Base' são mapeadas para tabelas no banco de dados
    """

    """
    Nome da tabela no banco
    """
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(125), nullable=False)

    description = Column(String(1024))

    done = Column(Boolean('done_contraint'))

    def __init__(self, name, description, done):
        self.name = name
        self.description = description,
        self.done = done if done is not None else False

    def __repr__(self):
        return ("<Task(id=%d, " % self.task_id
                + "name=%s, " % self.name
                + "description=%s, " % self.description
                + "done=%s)>" % self.done)

    def to_dict(self):
        return dict(
            name = self.name,
            description = self.description,
            done = self.done,
            id = self.task_id
        )


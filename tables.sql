CREATE TABLE papers (
	DOI INTEGER   NOT NULL,
	JID VARCHAR(10),
	CONSTRAINT paperspk PRIMARY KEY (DOI),
	CONSTRAINT paper_journalFk  FOREIGN KEY (JID) REFERENCES journals(JID)
);

CREATE TABLE journals (
	JID VARCHAR(10),
	economicativity_id_cnae INT NOT NULL,
	CONSTRAINT journalspk PRIMARY KEY (JID)
);
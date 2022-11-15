/**
 * Esquema inicial de la base de datos pialara previa a la visita al Victoria Kent
 */
/************************
 * Users
 ************************/

db.createCollection('users', {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            title: "Audio Object Validation",
            properties: {
                login: {
                    bsonType: "string",
                    description: "'login' must be a string"
                },
                password: {
                    bsonType: "string",
                    description: "'password' must be a string"
                },
                activo: {
                    bsonType: "bool",
                    description: "'activo' must be a boolean"
                },
                fecha_registro: {
                    bsonType: "string",
                    description: "'fecha_registro' must be a string"
                },
                nombre: {
                    bsonType: "string",
                    description: "'nombre' must be a string"
                },
                apellidos: {
                    bsonType: "string",
                    description: "'apellidos' must be a string"
                },
                fecha_nacimiento: {
                    bsonType: "timestamp",
                    description: "'fecha_nacimiento' must be a timestamp"
                },
                tipo: {
                    enum: ['usuario', 'admin', 'logopeda'],
                    description: "'tipo' must be a string"
                },
                usuarios_a_cargo: {
                    type: 'array',
                    items: {
                        type: 'string'
                    }
                },
                enfermedades: {
                    description: "Enfermedades del usuario",
                    type: "array",
                    items: {
                        type: 'object',
                        properties: {
                            nombre: {
                                bsonType: "string",
                                description: "'nombre' must be a string"
                            },
                            notas: {
                                bsonType: "string",
                                description: "'notas' must be a string"
                            },
                            nivel: {
                                bsonType: "int",
                                description: "'nivel' must be a int"
                            },
                            fecha_diagnostico: {
                                bsonType: "date",
                                description: "'fecha_diagnostico' must be a date"
                            },
                        }
                    }
                },

                disfonias: {
                    description: "Enfermedades del usuario",
                    type: "array",
                    items: {
                        type: 'object',
                        properties: {
                            nombre: {
                                bsonType: "string",
                                description: "'nombre' must be a string"
                            },
                            notas: {
                                bsonType: "string",
                                description: "'notas' must be a string"
                            },
                            nivel: {
                                bsonType: "int",
                                description: "'nivel' must be a int"
                            },
                            fecha_diagnostico: {
                                bsonType: "date",
                                description: "'fecha_diagnostico' must be a date"
                            },
                        }
                    }
                },
            }
        }

    }
});

/************************
 * Syllabus
 ************************/

db.createCollection('syllabus', {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            title: "Audio Object Validation",
            properties: {
                frase: {
                    bsonType: "string",
                    description: "'frase' must be a string"
                },
                dificultad: {
                    bsonType: "int",
                    description: "'dificultad' must be a int"
                },
                disfonia: {
                    bsonType: "string",
                    description: "'disfonia' must be a string"
                },
                activo: {
                    bsonType: "bool",
                    description: "'activo' must be a bool"
                },
            }
        }
    }
});


/************************
 * Audios
 ************************/

db.createCollection('audios', {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            title: "Audio Object Validation",
            properties: {
                s3_object_id: {
                    bsonType: "string",
                    description: "'s3_object_id' must be a string"
                },
                size: {
                    bsonType: "long",
                    description: "'size' must be a long"
                },
                duracion: {
                    bsonType: "int",
                    description: "'duracion' must be a string"
                },
                fecha_hora: {
                    bsonType: "int",
                    description: "'fecha_hora' must be a string"
                },
                user: {
                    description: "Usuario que ha grabado el audio",
                    type: "object",
                    properties: {
                        _id: {
                            bsonType: "objectId",
                            description: "'_id' must be a objectId"
                        },
                        nombre: {
                            bsonType: "string",
                            description: "'nombre' must be a string"
                        },
                        apellidos: {
                            bsonType: "string",
                            description: "'apellidos' must be a string"
                        }
                    }
                },
                sylabus: {
                    description: "La frase grabada",
                    type: "object",
                    properties: {
                        _id: {
                            bsonType: "objectId",
                            description: "'_id' must be a objectId"
                        },
                        frase: {
                            bsonType: "string",
                            description: "'frase' must be a string"
                        },
                    }
                }

            }
        }
    }
})

/************************
 * Enfermedades
 ************************/

db.createCollection('enfermedades', {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            title: "Student Object Validation",
            properties: {
                nombre: {
                    bsonType: "string",
                    description: "'nombre' must be a string"
                }
            }
        }
    }
});


/************************
 * Disfonias
 ************************/

db.createCollection('disfonias', {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            title: "Student Object Validation",
            properties: {
                nombre: {
                    bsonType: "string",
                    description: "'nombre' must be a string"
                }
            }
        }
    }
});

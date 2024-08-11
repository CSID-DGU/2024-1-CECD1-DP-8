package com.cecd.dp.domain.influencer.entity;

import static com.querydsl.core.types.PathMetadataFactory.*;

import com.querydsl.core.types.dsl.*;

import com.querydsl.core.types.PathMetadata;
import javax.annotation.processing.Generated;
import com.querydsl.core.types.Path;
import com.querydsl.core.types.dsl.PathInits;


/**
 * QInfluencer is a Querydsl query type for Influencer
 */
@Generated("com.querydsl.codegen.DefaultEntitySerializer")
public class QInfluencer extends EntityPathBase<Influencer> {

    private static final long serialVersionUID = 1026681661L;

    public static final QInfluencer influencer = new QInfluencer("influencer");

    public final EnumPath<com.cecd.dp.type.AccountType> accountType = createEnum("accountType", com.cecd.dp.type.AccountType.class);

    public final StringPath category = createString("category");

    public final StringPath email = createString("email");

    public final StringPath graphId = createString("graphId");

    public final NumberPath<Long> id = createNumber("id", Long.class);

    public final ListPath<com.cecd.dp.domain.media.entity.Media, com.cecd.dp.domain.media.entity.QMedia> mediaList = this.<com.cecd.dp.domain.media.entity.Media, com.cecd.dp.domain.media.entity.QMedia>createList("mediaList", com.cecd.dp.domain.media.entity.Media.class, com.cecd.dp.domain.media.entity.QMedia.class, PathInits.DIRECT2);

    public final ListPath<com.cecd.dp.domain.meta.entity.Meta, com.cecd.dp.domain.meta.entity.QMeta> metaList = this.<com.cecd.dp.domain.meta.entity.Meta, com.cecd.dp.domain.meta.entity.QMeta>createList("metaList", com.cecd.dp.domain.meta.entity.Meta.class, com.cecd.dp.domain.meta.entity.QMeta.class, PathInits.DIRECT2);

    public final StringPath name = createString("name");

    public final StringPath nickname = createString("nickname");

    public final StringPath password = createString("password");

    public QInfluencer(String variable) {
        super(Influencer.class, forVariable(variable));
    }

    public QInfluencer(Path<? extends Influencer> path) {
        super(path.getType(), path.getMetadata());
    }

    public QInfluencer(PathMetadata metadata) {
        super(Influencer.class, metadata);
    }

}


package com.cecd.dp.domain.mediahashtag.entity;

import static com.querydsl.core.types.PathMetadataFactory.*;

import com.querydsl.core.types.dsl.*;

import com.querydsl.core.types.PathMetadata;
import javax.annotation.processing.Generated;
import com.querydsl.core.types.Path;
import com.querydsl.core.types.dsl.PathInits;


/**
 * QMediaHashTag is a Querydsl query type for MediaHashTag
 */
@Generated("com.querydsl.codegen.DefaultEntitySerializer")
public class QMediaHashTag extends EntityPathBase<MediaHashTag> {

    private static final long serialVersionUID = 53052563L;

    private static final PathInits INITS = PathInits.DIRECT2;

    public static final QMediaHashTag mediaHashTag = new QMediaHashTag("mediaHashTag");

    public final com.cecd.dp.domain.hashtag.entity.QHashTag hashTag;

    public final NumberPath<Long> id = createNumber("id", Long.class);

    public final com.cecd.dp.domain.media.entity.QMedia media;

    public QMediaHashTag(String variable) {
        this(MediaHashTag.class, forVariable(variable), INITS);
    }

    public QMediaHashTag(Path<? extends MediaHashTag> path) {
        this(path.getType(), path.getMetadata(), PathInits.getFor(path.getMetadata(), INITS));
    }

    public QMediaHashTag(PathMetadata metadata) {
        this(metadata, PathInits.getFor(metadata, INITS));
    }

    public QMediaHashTag(PathMetadata metadata, PathInits inits) {
        this(MediaHashTag.class, metadata, inits);
    }

    public QMediaHashTag(Class<? extends MediaHashTag> type, PathMetadata metadata, PathInits inits) {
        super(type, metadata, inits);
        this.hashTag = inits.isInitialized("hashTag") ? new com.cecd.dp.domain.hashtag.entity.QHashTag(forProperty("hashTag")) : null;
        this.media = inits.isInitialized("media") ? new com.cecd.dp.domain.media.entity.QMedia(forProperty("media"), inits.get("media")) : null;
    }

}


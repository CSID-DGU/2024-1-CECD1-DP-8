package com.cecd.dp.domain.meta.entity;

import static com.querydsl.core.types.PathMetadataFactory.*;

import com.querydsl.core.types.dsl.*;

import com.querydsl.core.types.PathMetadata;
import javax.annotation.processing.Generated;
import com.querydsl.core.types.Path;
import com.querydsl.core.types.dsl.PathInits;


/**
 * QMeta is a Querydsl query type for Meta
 */
@Generated("com.querydsl.codegen.DefaultEntitySerializer")
public class QMeta extends EntityPathBase<Meta> {

    private static final long serialVersionUID = 2146592653L;

    private static final PathInits INITS = PathInits.DIRECT2;

    public static final QMeta meta = new QMeta("meta");

    public final com.cecd.dp.global.QBaseEntity _super = new com.cecd.dp.global.QBaseEntity(this);

    //inherited
    public final DateTimePath<java.time.LocalDateTime> createdAt = _super.createdAt;

    public final NumberPath<Integer> followerCnt = createNumber("followerCnt", Integer.class);

    public final NumberPath<Long> id = createNumber("id", Long.class);

    public final com.cecd.dp.domain.influencer.entity.QInfluencer influencer;

    public final NumberPath<Integer> likeAvg = createNumber("likeAvg", Integer.class);

    public final NumberPath<Integer> replyAvg = createNumber("replyAvg", Integer.class);

    //inherited
    public final DateTimePath<java.time.LocalDateTime> updatedAt = _super.updatedAt;

    public QMeta(String variable) {
        this(Meta.class, forVariable(variable), INITS);
    }

    public QMeta(Path<? extends Meta> path) {
        this(path.getType(), path.getMetadata(), PathInits.getFor(path.getMetadata(), INITS));
    }

    public QMeta(PathMetadata metadata) {
        this(metadata, PathInits.getFor(metadata, INITS));
    }

    public QMeta(PathMetadata metadata, PathInits inits) {
        this(Meta.class, metadata, inits);
    }

    public QMeta(Class<? extends Meta> type, PathMetadata metadata, PathInits inits) {
        super(type, metadata, inits);
        this.influencer = inits.isInitialized("influencer") ? new com.cecd.dp.domain.influencer.entity.QInfluencer(forProperty("influencer")) : null;
    }

}


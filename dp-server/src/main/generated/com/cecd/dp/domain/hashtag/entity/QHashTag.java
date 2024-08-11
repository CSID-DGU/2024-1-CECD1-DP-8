package com.cecd.dp.domain.hashtag.entity;

import static com.querydsl.core.types.PathMetadataFactory.*;

import com.querydsl.core.types.dsl.*;

import com.querydsl.core.types.PathMetadata;
import javax.annotation.processing.Generated;
import com.querydsl.core.types.Path;
import com.querydsl.core.types.dsl.PathInits;


/**
 * QHashTag is a Querydsl query type for HashTag
 */
@Generated("com.querydsl.codegen.DefaultEntitySerializer")
public class QHashTag extends EntityPathBase<HashTag> {

    private static final long serialVersionUID = -1634199799L;

    public static final QHashTag hashTag = new QHashTag("hashTag");

    public final NumberPath<Long> id = createNumber("id", Long.class);

    public final ListPath<com.cecd.dp.domain.mediahashtag.entity.MediaHashTag, com.cecd.dp.domain.mediahashtag.entity.QMediaHashTag> mediaHashTagList = this.<com.cecd.dp.domain.mediahashtag.entity.MediaHashTag, com.cecd.dp.domain.mediahashtag.entity.QMediaHashTag>createList("mediaHashTagList", com.cecd.dp.domain.mediahashtag.entity.MediaHashTag.class, com.cecd.dp.domain.mediahashtag.entity.QMediaHashTag.class, PathInits.DIRECT2);

    public final StringPath name = createString("name");

    public QHashTag(String variable) {
        super(HashTag.class, forVariable(variable));
    }

    public QHashTag(Path<? extends HashTag> path) {
        super(path.getType(), path.getMetadata());
    }

    public QHashTag(PathMetadata metadata) {
        super(HashTag.class, metadata);
    }

}


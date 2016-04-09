library(igraph)

ga.data <- read.csv('C:/Users/Guy Gonen/PycharmProjects/TweeterNetwork/edges_no_duplicates.csv', header = T)
head(ga.data)
g <- graph.data.frame(ga.data,directed = F)
g <- simplify(g)


V(g)$name
head(E(g))

g$layout <- layout.fruchterman.reingold(g)
plot(g)

degr.score <- degree(g)
degr.score

V(g)$size <- degree(g) * 0.2 # multiply by 2 for scale 
plot(g) 

V(g)$label <- NA # remove labels for now 
plot(g)


## Closeness centrality.
clo <- closeness(g) 
# rescale values to match the elements of a color vector 
clo.score <- round( (clo - min(clo)) * length(clo) / max(clo) ) + 1 
# create color vector, use rev to make red "hot" 
clo.colors <- rev(heat.colors(max(clo.score))) 
V(g)$color <- clo.colors[ clo.score ] 
plot(g)

## Betweeness centrality.
btw <- betweenness(g) 
btw.score <- round(btw) + 1 
btw.colors <- rev(heat.colors(max(btw.score))) 
V(g)$color <- btw.colors[ btw.score ] 
plot(g)

gnc <- edge.betweenness.community(g, directed=FALSE)
V(g)$color <- gnc$membership
V(g)$size <- 5 # Set same size to all nodes
plot(g)

V(g)$label <- NA # remove labels for now 
g$layout <- layout.kamada.kawai(g)
plot(g)


no.clusters(g)
## [1] 3
cl <- clusters(g)
which.max(cl$csize)
## [1] 1
cl$membership == which.max(cl$csize)
to.keep <- which(cl$membership == which.max(cl$csize))
g_gc <- induced.subgraph(g, to.keep)
summary(g_gc)
## IGRAPH UN-- 24 28 -- 
## attr: name (v/c), gender (v/c), size (v/n), color (v/c)
g_gc$layout <- layout.sphere(g_gc)
plot(g_gc)

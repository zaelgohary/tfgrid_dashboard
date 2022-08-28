import { RouteConfig } from "vue-router";

export const bootstrapRouter: RouteConfig[] = [
  {
    path: "/bootstrap/",
    name: "Bootstrap",
    component: () => import("../views/Bootstrap.vue"),
  }
];

class UrlMappings {

	static mappings = {
        "/$controller/$action?/$id?(.$format)?"{
            constraints {
                // apply constraints here
            }
        }

        "/"(controller:"info")
        "/filter/index"(controller:"filter")
        "/info/index"(controller:"info")
        "/demo/index"(controller:"demo")
        "500"(view:'/error')
	}
}

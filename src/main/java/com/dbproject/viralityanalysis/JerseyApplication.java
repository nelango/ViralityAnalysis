package com.dbproject.viralityanalysis;

import javax.inject.Inject;
import javax.servlet.ServletContext;
import javax.ws.rs.core.Context;

import com.fasterxml.jackson.jaxrs.json.JacksonJaxbJsonProvider;
import org.glassfish.hk2.api.ServiceLocator;
import org.glassfish.jersey.server.ResourceConfig;

/**
 * This handles setting up Jersey to handle requests and automatically converting request bodies and input parameters
 * into Java Bean objects using Jackson.  We also set up Guice in here to work with our Jersey Web Services so that we
 * can inject in any variety of services into our web services.
 */
public class JerseyApplication extends ResourceConfig {

    @Inject
    public JerseyApplication(@Context ServletContext servletContext, ServiceLocator serviceLocator) {

        //registers the Jackson stuff
        register(JacksonJaxbJsonProvider.class);
    }
}

for model in models:
    
    # Instantiate pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', model['clf'])
    ])
    
    # Instantiate and fit model using GridSearchCV
    cv = GridSearchCV(pipeline, param_grid=model['params'])
    cv.fit(X_train, y_train)
    
    # Make predictions
    y_pred = cv.predict(X_test)
    
    # Print classification report
    title = model['name'].replace('_', ' ').upper()
    print(title, '\n', classification_report(y_test, y_pred))
        
    # Save accuracy score
    accuracy_scores[title] = accuracy_score(y_test, y_pred)
    
    # Save model as pkl file
    filepath = f'data/{model["name"]}.pkl'
    with open(filepath, 'wb') as file:
        pickle.dump(cv, file)